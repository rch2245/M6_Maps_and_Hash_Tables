"""Defines the Schedule class which stores ScheduleItem objects in a dictionary."""

import csv

from schedule_item import ScheduleItem


class Schedule:
    """Stores course entries in a dict (hash table) keyed by Subject_Catalog_Section."""

    def __init__(self) -> None:
        self._items: dict[str, ScheduleItem] = {}

    def add_entry(self, item: ScheduleItem) -> None:
        """Add a ScheduleItem to the schedule using its unique key."""
        self._items[item.get_key()] = item

    def load_from_csv(self, filename: str) -> None:
        """Load course rows from a CSV file using csv.DictReader.

        The CSV is treated as read-only; this method only reads from it.
        """
        with open(filename, encoding="utf-8-sig", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = ScheduleItem(
                    subject=row["Subject"].strip(),
                    catalog=row["Catalog"].strip(),
                    section=row["Section"].strip(),
                    component=row["Component"].strip(),
                    session=row["Session"].strip(),
                    units=_to_int(row.get("Units")),
                    tot_enrl=_to_int(row.get("TotEnrl")),
                    cap_enrl=_to_int(row.get("CapEnrl")),
                    instructor=row["Instructor"].strip(),
                )
                self.add_entry(item)

    def print_header(self) -> None:
        """Print the column headers for the schedule report."""
        print(
            f"{'Subject':<8} {'Catalog':<8} {'Section':<8} "
            f"{'Component':<10} {'Session':<8} "
            f"{'Units':>5} {'TotEnrl':>8} {'CapEnrl':>8}  Instructor"
        )
        print("-" * 90)

    def print(self) -> None:
        """Print a full formatted schedule report."""
        self.print_header()
        for item in self._items.values():
            item.print()
        print(f"\nTotal entries: {len(self._items)}")

    def find_by_subject(self, subject: str) -> list[ScheduleItem]:
        """Return all items matching the given subject (case-insensitive)."""
        subject = subject.strip().upper()
        return [i for i in self._items.values() if i.subject.upper() == subject]

    def find_by_subject_catalog(self, subject: str, catalog: str) -> list[ScheduleItem]:
        """Return all items matching the given subject and catalog number."""
        subject = subject.strip().upper()
        catalog = catalog.strip()
        return [
            i
            for i in self._items.values()
            if i.subject.upper() == subject and i.catalog == catalog
        ]

    def find_by_instructor_last_name(self, last_name: str) -> list[ScheduleItem]:
        """Return all items whose instructor last name matches (case-insensitive).

        The CSV stores instructors as "Last,First"; we compare against the portion
        before the first comma.
        """
        last_name = last_name.strip().lower()
        return [
            i
            for i in self._items.values()
            if i.instructor.split(",")[0].strip().lower() == last_name
        ]

    def print_results(self, results: list[ScheduleItem]) -> None:
        """Print a header followed by a list of matching items."""
        if not results:
            print("No matching entries found.")
            return
        self.print_header()
        for item in results:
            item.print()
        print(f"\n{len(results)} match(es) found.")


def _to_int(value: str | None) -> int:
    """Safely convert a CSV cell to int; blank or non-numeric cells become 0."""
    if value is None:
        return 0
    value = value.strip()
    if not value:
        return 0
    try:
        return int(value)
    except ValueError:
        return 0
