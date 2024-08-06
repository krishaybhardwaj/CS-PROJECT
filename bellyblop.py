def bellyblop():
    import mysql.connector
    import os
    def blob_retrieve():
        
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'krishay',
            'database': 'blobtest'
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

       
        query = "SELECT pic FROM myimage WHERE picid = %s" 
        image_id = 3

        cursor.execute(query, (image_id,))
        image_data = cursor.fetchone()[0]

        output_folder = "output_images"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

  
        output_path = os.path.join(output_folder, f"output_image_{image_id}.jpg")

        
        with open(output_path, "wb") as output_file:
            output_file.write(image_data)
            
        print("Uploaded successfully!")
        print("Please check the output_images folder for the image ")

        
        cursor.close()
        connection.close()
    #""C:\Users\krish\OneDrive\Pictures\Camera Roll\WIN_20230205_22_13_42_Pro.jpg""

    def blob_input():
    

       
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'krishay',
            'database': 'blobtest'
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = "INSERT INTO myimage (pic) VALUES (%s)"  

        
        input_image_path = input("Enter file path: ")
        

       
        with open(input_image_path, "rb") as image_file:
            image_data = image_file.read()

        
        cursor.execute(insert_query, (image_data,))
        connection.commit()

        print("Image data inserted successfully.")

        
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
