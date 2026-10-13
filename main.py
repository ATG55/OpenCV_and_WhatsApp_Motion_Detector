import cv2
import time
import pyautogui
import webbrowser
import os



def send_whatsapp_message():
    
    phone_number = ""
    timestamp = time.strftime("%d %H:%M")
    message=f"Hareket tespit edildi : {timestamp}"
    web_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"

    try:
        print(f"[INFO]  Whatsapp üzerinden mesaj gönderiliyor : {message}")
        webbrowser.open(web_url)
        time.sleep(12)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
    except Exception as e:
        print("[ERROR]  Mesaj gönderilirken bir hata meydana geldi")
        return False

def main():
    pyautogui.PAUSE = 1.5
    phone_number = "90"+ input("Phone number : ")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR]  Kamera acilamadi")
        return
    BackSub = cv2.createBackgroundSubtractorMOG2(
        history=500,
        varThreshold=16,
        detectShadows=True
    )
    last_motion_time = 0
    cooldown = 10
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR]  Kamera görüntüsü alinamadi")
            break
        fgMask = BackSub.apply(frame)
        _ , thresh = cv2.threshold(fgMask,127,255,cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh,None,iterations=2)
        thresh = cv2.dilate(thresh,None,iterations=2)


        contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < 1500:
                continue
            motion_detected = True
            break
        current_time = time.time()


        if motion_detected and (current_time-last_motion_time>cooldown):
            print("[INFO]  Hareket algilandi")
            if send_whatsapp_message():
                last_motion_time = current_time
                cv2.putText(frame,"Hareket Algılandı",(10,30),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8, (255, 0, 0), 2)
                time.sleep(1)
            else:
                print("[ERROR]  Mesaj gönderilemedi")
                time.sleep(5)
        else:
            cv2.putText(frame,"Hareket Algılanamadı",(10,30),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8, (255, 0, 0), 2)

        cv2.imshow("kamera",frame)
        cv2.imshow("hareket maskesi",thresh)

        if cv2.waitKey(1)&0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()