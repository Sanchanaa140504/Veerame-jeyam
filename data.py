

import sqlite3
from typing import Any, Iterator


def filter_students(
	database: str,
	*,
	name: str | None = None,
	age: int | None = None,
	grade: str | None = None,
	course: str | None = None,
	limit: int = 100,
	offset: int = 0,
) -> Iterator[dict[str, Any]]:
	"""Yield matching students without loading the complete table into memory.

	Expects a ``students`` table with columns ``id``, ``name``, ``age``,
	``grade`` and ``course``. Values are bound parameters to avoid SQL injection.
	"""
	if limit <= 0 or offset < 0:
		raise ValueError("limit must be positive and offset cannot be negative")

	conditions: list[str] = []
	parameters: list[Any] = []

	if name:
		conditions.append("name LIKE ? COLLATE NOCASE")
		parameters.append(f"%{name}%")
	if age is not None:
		conditions.append("age = ?")
		parameters.append(age)
	if grade:
		conditions.append("grade = ?")
		parameters.append(grade)
	if course:
		conditions.append("course = ?")
		parameters.append(course)

	query = "SELECT id, name, age, grade, course FROM students"
	if conditions:
		query += " WHERE " + " AND ".join(conditions)
	query += " ORDER BY id LIMIT ? OFFSET ?"
	parameters.extend((limit, offset))

	with sqlite3.connect(database) as connection:
		connection.row_factory = sqlite3.Row
		for row in connection.execute(query, parameters):
			yield dict(row)
