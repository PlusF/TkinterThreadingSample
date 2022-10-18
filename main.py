import tkinter as tk
import threading
import time


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # ウィジェット作成
        self.number = tk.IntVar(value=0)
        self.label_number = tk.Label(master, textvariable=self.number)
        self.button_quit = tk.Button(master, text='QUIT', command=self.quit)
        self.label_number.pack()
        self.button_quit.pack()

        # スレッド
        self.quit_flag = False
        self.thread = threading.Thread(target=self.infinite_func)
        self.thread.start()

    def infinite_func(self):
        while not self.quit_flag:
            # 数を1ずつ増やす
            self.number.set(self.number.get() + 1)
            time.sleep(1)

    def quit(self):
        # フラグを立てる
        self.quit_flag = True
        # スレッドの終了を待つ（ウィンドウを閉じる前に！）
        self.thread.join()
        # ウィンドウを閉じる
        self.master.destroy()


def main():
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())  # QUITボタン以外の終了操作を許可しない
    app = App(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
