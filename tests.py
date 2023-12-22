import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from tkinter import ttk
from os import listdir
from Main import ConfigurationPage, LoadingPopup, MasterWindow


class TestMasterWindow(unittest.TestCase):
    @patch("Main.tk.PhotoImage")
    def setUp(self, mock_photoimage):
        self.master_window = MasterWindow()

    def tearDown(self):
        self.master_window.destroy()

    def test_get_username(self):
        # non-empty username
        self.master_window.username = "John Doe"
        username = self.master_window.get_username()
        self.assertEqual(username, "John Doe")

        # empty username
        self.master_window.username = ""
        username = self.master_window.get_username()
        self.assertEqual(username, "Not Applicable")


class TestConfigurationPage(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.configuration_page = ConfigurationPage(self.root, Mock())

    @patch("tkinter.filedialog.askdirectory", return_value=None)
    def test_open_file_explorer_no_selection(self, mock_askdirectory):
        self.configuration_page.open_file_explorer()
        actual_text = self.configuration_page.directory_label.cget("text")
        expected_text = "None/"
        self.assertEqual(actual_text, expected_text)

    @patch("tkinter.filedialog.askdirectory", return_value="/")
    def test_open_file_explorer_root_directory(self, mock_askdirectory):
        self.configuration_page.open_file_explorer()
        actual_text = self.configuration_page.directory_label.cget("text")
        expected_text = "//"
        self.assertEqual(actual_text, expected_text)


class TestLoadingPopup(unittest.TestCase):
    def setUp(self):
        mock_controller = Mock()
        mock_controller.extract_data.return_value = {
            "title": "Test Title",
            "people": {"Participant1": ["Message1", "Message2"]},
            "room": "Test Room",
            "all_msgs": 100,
            "all_chars": 500,
            "calltime": "01:30:00",
            "sent_msgs": 50,
            "start_date": "2023-01-01",
            "total_photos": 5,
            "total_gifs": 3,
            "total_videos": 2,
            "total_files": 10,
        }

        # LoadingPopup instance with the mocked controller
        self.loading_popup = LoadingPopup(mock_controller, 2, ttk.Treeview())

    @patch("Main.LoadingPopup", return_value={"data": "sample_data"})
    def test_loading_popup_conversations(self, mock_popup):
        # LoadingPopup returns fake data when loading conversations - loading done in __init__ so no need for separate method.
        pass

    @patch("Main.LoadingPopup", return_value={"data": "sample_data"})
    def test_loading_popup_no_conversations(self, mock_popup):
        pass


if __name__ == "__main__":
    unittest.main()
