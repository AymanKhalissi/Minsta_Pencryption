The repository for this project, named "Minsta Middleware", is a Python-based project that provides encryption and decryption services for a database, specifically for the Minsta application.

Here's a brief description of the main components of the repository:

main.py: This is the main script of the project. It prompts the user for input, handles the encryption/decryption process, and logs the metrics.

Pencryption.py: This file serves as a library for the project. It contains the decrypt_column function, which is used to decrypt a specified column from a database table.

user_data_operations.py: This file contains functions for extracting and inserting user data from/into the database, as well as counting the number of users.

metrics.py: This file contains functions for calculating and logging metrics related to the encryption/decryption process.

data_cipher.py: This file contains the DataCipher class, which is used for encrypting and decrypting data.

database_connection.py: This file contains the DatabaseConnection class, which is used for managing database connections.

utils.py: This file contains utility functions, such as get_key_from_file, which is used to retrieve the encryption key from a file.

The repository also includes a requirements.txt file for managing Python dependencies, and a README.md file that provides an overview of the project and instructions for installation and usage.

The project uses symmetric encryption to secure user data and includes functionality for calculating and logging metrics related to the encryption and decryption process. It is designed to be used with a PostgreSQL database.