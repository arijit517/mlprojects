# Let's create a test to replicate and debug the DataIngestion class behavior
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Dummy class to simulate logging for clarity in notebook
class logging:
    @staticmethod
    def info(msg):
        print(f"[INFO]: {msg}")

# Simulating CustomException for simplicity
class CustomException(Exception):
    def __init__(self, message, sys_info):
        super().__init__(f"{message} | SYS INFO: {sys_info}")

# Configuration for data ingestion paths
class DataIngestionConfig:
    def __init__(self):
        self.train_data_path = os.path.join('artifacts', "train.csv")
        self.test_data_path = os.path.join('artifacts', "test.csv")
        self.raw_data_path = os.path.join('artifacts', "data.csv")

# Data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Use a dummy dataframe instead of reading a file
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Created a sample dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Saved raw data")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, "Mock sys info")

# Instantiate and run the data ingestion process
obj = DataIngestion()
train_data_path, test_data_path = obj.initiate_data_ingestion()
(train_data_path, test_data_path)
                 