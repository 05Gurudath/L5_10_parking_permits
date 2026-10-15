
"""Manage parking permits, zone checks, and permit persistence."""

import json
import secrets
from datetime import datetime, timedelta
from pathlib import Path

permits = {}
ZONES = ["A", "B", "C"]


def register_permit(vehicle_plate, zone_id, zone_records=None):
    """Register a valid vehicle plate for an authorized parking zone."""
    if not isinstance(vehicle_plate, str) or not vehicle_plate.strip():
        return None

    if zone_id not in ZONES:
        return None

    if zone_records is None:
        zone_records = []

    permit_no = f"P{secrets.randbelow(90000) + 10000}"
    expiry = datetime.now() + timedelta(days=180)

    permits[vehicle_plate] = {
        "zone": zone_id,
        "permit": permit_no,
        "expiry": expiry.strftime("%Y-%m-%d"),
    }
    zone_records.append((vehicle_plate, zone_id))
    return permit_no


def revoke_permit(vehicle_plate):
    """Revoke a permit if it exists."""
    permits.pop(vehicle_plate, None)


def is_expired(vehicle_plate):
    """Return whether a known permit has expired."""
    try:
        expiry_text = permits[vehicle_plate]["expiry"]
        expiry = datetime.strptime(expiry_text, "%Y-%m-%d")
    except (KeyError, TypeError, ValueError):
        return False

    return expiry.date() < datetime.now().date()


def scan_zone(zone_id, plates_seen):
    """Return plates that are unauthorized or expired in a zone."""
    flagged = []

    for plate in plates_seen:
        if (
            plate not in permits
            or permits[plate]["zone"] != zone_id
            or is_expired(plate)
        ):
            flagged.append(plate)

    return flagged


def load_permit_database(file="permits.json"):
    """Load permit records from a JSON file."""
    try:
        with Path(file).open("r", encoding="utf-8") as database:
            data = json.load(database)
    except (OSError, json.JSONDecodeError):
        permits.clear()
        return

    if isinstance(data, dict):
        permits.clear()
        permits.update(data)
    else:
        permits.clear()


def save_permit_database(file="permits.json"):
    """Save permit records to a JSON file."""
    with Path(file).open("w", encoding="utf-8") as database:
        json.dump(permits, database, indent=4)


def set_expiry(vehicle_plate, date_text):
    """Set a permit's expiry date using YYYY-MM-DD format."""
    if vehicle_plate not in permits:
        return False

    try:
        expiry = datetime.strptime(date_text, "%Y-%m-%d")
    except (TypeError, ValueError):
        return False

    permits[vehicle_plate]["expiry"] = expiry.strftime("%Y-%m-%d")
    return True


def main():
    """Run the parking permit manager demonstration."""
    load_permit_database()
    register_permit("KA01AB1234", "A")
    register_permit("KA05XY9999", "Z")
    register_permit("", "B")
    register_permit(None, "C")
    set_expiry("KA01AB1234", "2020-01-01")
    revoke_permit("MH12ZZ0000")

    print(
        "Flagged in zone A:",
        scan_zone(
            "A",
            ["KA01AB1234", "KA05XY9999", "TN09QQ1111"],
        ),
    )

    plate = input("Plate to revoke (Enter to skip): ")
    if plate:
        revoke_permit(plate)

    save_permit_database()
    print("Permits on file:", len(permits))


if __name__ == "__main__":
    main()
