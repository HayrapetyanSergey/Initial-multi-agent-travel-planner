def estimate_budget(parsed_data, research_data, itinerary_data):
    """
    Budget Agent:
    Estimates trip costs using parsed user budget and local research data.
    Handles missing or non-numeric budget values gracefully.
    """

    duration_days = parsed_data.get("duration_days") or 1
    user_budget = parsed_data.get("budget")

    try:
        duration_days = int(duration_days)
    except Exception:
        duration_days = 1

    try:
        if user_budget is not None:
            user_budget = float(user_budget)
    except Exception:
        user_budget = None

    if research_data.get("status") != "success":
        return {
            "budget_status": "Cannot estimate budget",
            "reason": "Research data is missing or destination was not found.",
            "user_budget": user_budget,
            "estimated_costs": None
        }

    daily_costs = research_data.get("daily_cost_estimates", {})

    hotel_daily = daily_costs.get("hotel", 0)
    food_daily = daily_costs.get("food", 0)
    transport_daily = daily_costs.get("transport", 0)

    matched_places = research_data.get("matched_places", [])

    activity_cost = sum(place.get("estimated_cost", 0) for place in matched_places)

    hotel_total = hotel_daily * duration_days
    food_total = food_daily * duration_days
    transport_total = transport_daily * duration_days
    total_estimated_cost = hotel_total + food_total + transport_total + activity_cost

    if user_budget is None:
        budget_status = "Budget was not provided as a clear number."
        remaining_budget = None
    else:
        remaining_budget = user_budget - total_estimated_cost
        budget_status = "Within budget" if remaining_budget >= 0 else "Over budget"

    return {
        "duration_days": duration_days,
        "user_budget": user_budget,
        "estimated_costs": {
            "hotel_total": hotel_total,
            "food_total": food_total,
            "transport_total": transport_total,
            "activities_total": activity_cost,
            "total_estimated_cost": total_estimated_cost
        },
        "remaining_budget": remaining_budget,
        "budget_status": budget_status,
        "note": "Costs are approximate and based on the local knowledge base, not live prices."
    }