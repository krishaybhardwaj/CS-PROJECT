import mysql.connector

def combine_tables():
    # Connect to the MySQL database
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'krishay',
        'database': 'latecomers'
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Query to combine tables and add columns from blobtest to student
    combine_query = """
    ALTER TABLE student
    ADD COLUMN new_column_name DATATYPE;  -- Replace DATATYPE with the appropriate data type

    UPDATE student s
    INNER JOIN blobtest b ON s.student_id = b.student_id  -- Replace student_id with the appropriate column name
    SET s.new_column_name = b.blob_column_name;  -- Replace new_column_name and blob_column_name

    ALTER TABLE student
    DROP COLUMN new_column_name;
    """
    
    cursor.execute(combine_query)
    connection.commit()

    print("Tables combined and columns added successfully.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

combine_tables()
