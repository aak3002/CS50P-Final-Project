import os
import pytest
from diary import write_entry, save_entry, read_entries, edit_entry

@pytest.fixture
def diary_file(tmp_path):
    return tmp_path / "diary.txt"

def test_write_entry(diary_file, monkeypatch):
    test_input = "This is a test entry."
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    write_entry()
    assert diary_file.read_text().strip() == f"Date: {diary_file.stat().st_mtime}\n\n{test_input}\n"

def test_save_entry(diary_file):
    test_entry = "Test entry content."
    save_entry(test_entry)
    assert diary_file.read_text().strip() == f"Date: {diary_file.stat().st_mtime}\n\n{test_entry}\n"

def test_read_entries_empty(diary_file, capsys):
    read_entries()
    captured = capsys.readouterr()
    assert "No entries found." in captured.out

def test_read_entries_with_entries(diary_file, capsys):
    test_entry = "Test entry content."
    with open(diary_file, "w") as file:
        file.write(f"Date: {diary_file.stat().st_mtime}\n\n{test_entry}\n")
    read_entries()
    captured = capsys.readouterr()
    assert test_entry in captured.out

def test_edit_entry_invalid_input(monkeypatch, capsys, diary_file):
    with open(diary_file, "w") as file:
        file.write(f"Date: {diary_file.stat().st_mtime}\n\nInitial entry content.\n")
    monkeypatch.setattr('builtins.input', lambda _: "invalid")
    edit_entry()
    captured = capsys.readouterr()
    assert "Invalid entry number." in captured.out

def test_edit_entry_valid_input(monkeypatch, diary_file):
    initial_entry = "Initial entry content."
    new_entry = "Edited entry content."
    with open(diary_file, "w") as file:
        file.write(f"Date: {diary_file.stat().st_mtime}\n\n{initial_entry}\n")
    monkeypatch.setattr('builtins.input', lambda _: new_entry)
    edit_entry()
    assert new_entry in diary_file.read_text()

if __name__ == "__main__":
    pytest.main([__file__])
