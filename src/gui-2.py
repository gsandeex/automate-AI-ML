import dearpygui.dearpygui as dpg


def run_python_code(sender, app_data):
    input_value1 = dpg.get_value("Input1")
    input_value2 = dpg.get_value("Input2")
    # Call your Python function with the input values
    print("Input 1:", input_value1)
    print("Input 2:", input_value2)


with dpg.create_viewport(title="Input GUI", width=500, height=200):
    with dpg.create_window(title="Input Window", width=500, height=200):
        dpg.add_input_text("Input1", label="Input 1", default_value="")
        dpg.add_input_text("Input2", label="Input 2", default_value="")
        dpg.add_button(label="Run Python Code", callback=run_python_code)

dpg.start_dearpygui()

