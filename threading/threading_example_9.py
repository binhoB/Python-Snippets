import threading

def my_func():
  print("It works!")
  print("Finished :)")

if __name__ == "__main__":
  print("Before calling my_func")
  t = threading.Timer(5.0, my_func)
  t.start()