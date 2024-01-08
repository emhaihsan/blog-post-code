import cv2
import numpy as np


def warna_dominan(frame):
    b, g, r = cv2.split(frame)

    bm = np.mean(b)
    gm = np.mean(g)
    rm = np.mean(r)

    if max(bm, gm, rm) == bm:
        return "Biru"
    elif max(bm, gm, rm) == gm:
        return "Hijau"
    else:
        return "Merah"


def main():
    vid = cv2.VideoCapture(0)

    while True:
        _, frame = vid.read()

        warna = warna_dominan(frame)

        cv2.putText(frame, "Warna dominan: " + warna, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
