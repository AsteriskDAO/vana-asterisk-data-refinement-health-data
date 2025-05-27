import json
import logging
import os
import sys
import traceback
import zipfile

from refiner.refine import Refiner
from refiner.config import settings

logging.basicConfig(level=logging.INFO, format='%(message)s')


def run() -> None:
    """Transform all input files into the database."""
    input_files_exist = os.path.isdir(settings.INPUT_DIR) and bool(os.listdir(settings.INPUT_DIR))

    if not input_files_exist:
        raise FileNotFoundError(f"No input files found in {settings.INPUT_DIR}")
    logging.info(f"Input files exist")
    extract_input()
    logging.info(f"Extracted input files")
    refiner = Refiner()
    logging.info(f"Initialized Refiner")
    output = refiner.transform()
    logging.info(f"Transformed input files")
    output_path = os.path.join(settings.OUTPUT_DIR, "output.json")
    with open(output_path, 'w') as f:
        json.dump(output.model_dump(), f, indent=2)    
    logging.info(f"Data transformation complete: {output}")


def extract_input() -> None:
    """
    If the input directory contains any zip files, extract them
    :return:
    """
    for input_filename in os.listdir(settings.INPUT_DIR):
        input_file = os.path.join(settings.INPUT_DIR, input_filename)

        # Check if file is actually JSON despite the extension
        try:
            with open(input_file, 'r') as f:
                logging.info(f"Processing {input_filename} in extract_input")
                json.load(f)  # Try to parse as JSON
                if input_filename.lower().endswith('.zip'):
                    # It's a JSON file with wrong extension, rename it
                    new_filename = input_filename[:-4] + '.json'
                    new_path = os.path.join(INPUT_DIR, new_filename)
                    os.rename(input_file, new_path)
                    logging.info(f"Renamed {input_filename} to {new_filename} as it contains JSON data")
                continue
        except json.JSONDecodeError:
            pass  # Not JSON, continue with ZIP check
        
        # Handle actual ZIP files
        if zipfile.is_zipfile(input_file):
            logging.info(f"Extracting ZIP file {input_filename}")
            try:
                with zipfile.ZipFile(input_file, 'r') as zip_ref:
                    zip_ref.extractall(INPUT_DIR)
                logging.info(f"Extracted {input_filename}")
            except zipfile.BadZipFile as e:
                logging.error(f"Failed to extract {input_filename}: {str(e)}")





if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        traceback.print_exc()
        sys.exit(1)
