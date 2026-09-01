# =========================================================
# AIRPORTS
# =========================================================

GET_AIRPORTS = """
SELECT airport
FROM airports
ORDER BY airport
"""

GET_AIRPORT = """
SELECT
    airport,
    airport_id,
    city,
    state
FROM airports
WHERE airport = ?
"""

# =========================================================
# AIRLINES
# =========================================================

GET_AIRLINES = """
SELECT carrier
FROM airlines
ORDER BY carrier
"""

# =========================================================
# ROUTES
# =========================================================

GET_ROUTE = """
SELECT
    origin,
    destination,
    distance,
    distance_group,
    crs_elapsed_time
FROM routes
WHERE origin = ?
AND destination = ?
"""

# =========================================================
# PREDICTIONS
# =========================================================

INSERT_PREDICTION = """
INSERT INTO predictions (

    timestamp,
    airline,
    origin,
    destination,
    probability,
    prediction

)

VALUES (?, ?, ?, ?, ?, ?)
"""

GET_PREDICTIONS = """
SELECT *
FROM predictions
ORDER BY timestamp DESC
"""

DELETE_PREDICTIONS = """
DELETE FROM predictions
"""