import multiprocessing
import os
import time

def second_script_callback():
    print("Second script finished!")

def run_second_script():
    # Import the second script to avoid code duplication
    from second_script import generate_and_save_plot
    
    generate_and_save_plot()
    
    # Notify the main script that the second script has finished
    second_script_callback()

if __name__ == "__main__":
    # Start the second script in a separate process
    process = multiprocessing.Process(target=run_second_script)
    process.start()


    

    # Wait for the second script to finish and notify
    process.join()

    # Open the generated image using the default image viewer
    image_path = "plot.png"
    if os.path.exists(image_path):
        os.startfile(image_path)
    else:
        print("Image not found.")

