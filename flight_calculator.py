"""
A commercial quadcopter's battery is rated for up to 8 hours of standby/idle operation, 
but its real-world usable active flight time — with no payload attached — is only 3 hours 
(180 minutes), since active flight draws far more power than standby. 
As payload weight increases, active flight time decreases linearly, following:

T(w) = 180 - 0.1w

where T is the resulting active flight time in minutes, and w is the payload weight in grams 
(w ≥ 0). Note that the 8-hour standby rating is background context only — it is not part 
of the calculation; only the 180-minute active-flight baseline and the 
formula above are used.    
"""

def calculate_flight_time(weight_grams):
    """Return active flight time in minutes for a payload weight in grams."""
    if weight_grams < 0:
        raise ValueError("weight_grams must be non-negative")

    return max(0.0, 180.0 - 0.1 * weight_grams)


def flight_time_table(max_weight_grams, step_grams):
    """Return a list of (weight_grams, flight_minutes) rows from 0 to max_weight_grams."""
    if max_weight_grams < 0:
        raise ValueError("max_weight_grams must be non-negative")
    if step_grams <= 0:
        raise ValueError("step_grams must be positive")

    """
    while current_weight <= max_weight_grams + 1e-9:
        values.append((current_weight, calculate_flight_time(current_weight)))
        current_weight += step_grams
    """
    # Copilot suggested a while loop with an accumulating counter and an epsilon
    # on the bound I edited this to use range() to avoid float drift and drop the epsilon.
    values = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        values.append((weight, calculate_flight_time(weight)))
    return values
