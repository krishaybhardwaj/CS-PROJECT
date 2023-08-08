def bellyblop():
    import mysql.connector
    import os
    def blob_retrieve():
        # Connect to the MySQL database
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'krishay',
            'database': 'blobtest'
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Query to retrieve image data
        query = "SELECT pic FROM myimage WHERE picid = %s"  # Modify this query according to your table structure

        # Provide the ID of the row containing the image you want to retrieve
        image_id = 3

        cursor.execute(query, (image_id,))
        image_data = cursor.fetchone()[0]

        output_folder = "output_images"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Construct the output image path
        output_path = os.path.join(output_folder, f"output_image_{image_id}.jpg")

        # Write the image data to the output file in binary mode
        with open(output_path, "wb") as output_file:
            output_file.write(image_data)
            
        print("Uploaded successfully!")
        print("Please check the output_images folder for the image ")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    #""C:\Users\krish\OneDrive\Pictures\Camera Roll\WIN_20230205_22_13_42_Pro.jpg""

    def blob_input():
    

        # Connect to the MySQL database
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'krishay',
            'database': 'blobtest'
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Query to insert image data
        insert_query = "INSERT INTO myimage (pic) VALUES (%s)"  # Modify this query according to your table structure

        # Input image file path
        input_image_path = input("Enter file path: ")
        #"input_image.jpg"  # Change this to the path of your input image

        # Read image data from the input file
        with open(input_image_path, "rb") as image_file:
            image_data = image_file.read()

        # Insert the image data into the database
        cursor.execute(insert_query, (image_data,))
        connection.commit()

        print("Image data inserted successfully.")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    while True:
        print("~~MAIN MENU~~")
        print("1: input \n2: Display \n3: Exit")
        user_input=int(input("Choose a number: "))
        if user_input ==1:
            blob_input()
        elif user_input == 2:
            blob_retrieve()
        elif user_input == 3:
            print("Exiting program...")
            exit()
        else:
            print("Invalid response!")
        
bellyblop()