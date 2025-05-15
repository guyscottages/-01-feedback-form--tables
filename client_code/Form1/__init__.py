from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
   # Set Form properties and Data Bindings.
   self.init_components(**properties)

  def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    anvil.server.call('add_feedback', name, email, feedback)
    Notification("Feedback submitted!").show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = "Enter data"
    self.email_box.text = "Enter data"
    self.feedback_box.text = "Enter data"