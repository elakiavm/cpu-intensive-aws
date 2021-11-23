# from flask import Flask
from multiprocessing import Pool
from multiprocessing import cpu_count
import signal

# app =  Flask(__name__)

stop_loop = 0

# @app.route('/')

def exit_chld(x, y):

    global stop_loop

    stop_loop = 1

def f(x):

    global stop_loop

    while not stop_loop:

        x*x

signal.signal(signal.SIGINT, exit_chld)



if __name__ == '__main__':

    processes = cpu_count() 
    print('-' * 20)
    print('Running load on CPU(s)')
    print('Utilizing %d cores' % processes)
    print('-' * 20)
    pool = Pool(processes)
    pool.map(f, range(processes))

    # app.run(debug=True,host='0.0.0.0')