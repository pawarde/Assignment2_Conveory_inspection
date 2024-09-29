import cv2
from ultralytics import YOLO
import psycopg2
from psycopg2 import sql


# Load the YOLOv8 model
model = YOLO('/home/deepak/Desktop/29/ASS/MODEL/NEW/best.pt')
# Open the video
video_path = '/home/deepak/Desktop/29/ASS/VIDEO/TEST.mp4'
Output_Path="/home/deepak/Desktop/29/ASS/OUTPUT/DEFECT"

# Define database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'conveyor'
DB_USER = 'postgres'
DB_PASS = 'admin'

def insert_defect(defect):
    try:
        # Connect to PostgreSQL
        dbConnection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            dbname=DB_NAME
        )
        cur = dbConnection.cursor()
        
        # Use parameterized query to prevent SQL injection
        query = sql.SQL("INSERT INTO process (defect) VALUES (%s)").format()
        cur.execute(query, (defect,))  # Execute with the defect value
        
        dbConnection.commit()  # Commit the changes
    except Exception as e:
        print("insert_defect() Exception is: " + str(e))
    finally:
        cur.close()  # Close cursor
        dbConnection.close()  # Close the database connection

def main():
    cap = cv2.VideoCapture(video_path)  
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Run the model on the frame
        results = model.predict(frame)
        # Check if there are any detected boxes
        if results and results[0].boxes is not None and len(results[0].boxes) > 0:
            for result in results[0].boxes:
                conf = result.conf[0]  # Confidence score
                cls = int(result.cls[0])  # Class id
                label = model.names[cls]  # Get label name
                x1, y1, x2, y2 = map(int, result.xyxy[0])
                if conf > 0.3:  # Set a confidence threshold
                    if label=="PATCH" and  x1 >111 and y1 >240 :
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        insert_defect(defect=label)
                        cv2.imwrite(f"{Output_Path}/DEFECT_TMP.jpg",frame)
            
        else:
            print("No objects detected.")


main()