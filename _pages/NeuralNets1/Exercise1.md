---
layout: exercise_pyodide
permalink: "NeuralNets1/Exercise1"
title: "IDS 301: Neural Nets 1: Grid Search"
excerpt: "IDS 301: Neural Nets 1: Grid Search"
canvasasmtid: "174475"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "<p></p>"
  packages: "numpy"
  goals:
    - To use grid search to find the optimal function in a family of functions to fit labeled data
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ref = 0.5375;
    let tol = 0.1
  correctcheck: |
    Math.abs(pyodide.globals.res - ref) < tol
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.res == 0
      feedback: "Try again.  It looks like you're still returning c=0, but you need to find the c that minimizes the loss function" 

files:

  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 400
    code: | 
        import numpy as np

        def fc(c, x):
            return np.array(x > c, dtype=float)

        def loss_squared(X, Y, f):
            return np.sum((Y - f(X))**2)

        def grid_search(X, Y):
            cs = np.linspace(-3, 3, 1000)
            losses = np.zeros_like(cs)
            for i in range(len(cs)):
                c = cs[i]
                f = lambda x: fc(c=c, x=X)
                losses[i] = loss_squared(X, Y, f)
            ## TODO: Return the c that minimizes the squared loss

            return 0 # TODO: This is a dummy



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        N = 50
        np.random.seed(0)
        # X is data, Y is labels 
        X = np.random.randn(N) - 1
        Y = np.zeros(N)
        X = np.concatenate((X, np.random.randn(N)+2))
        Y = np.concatenate((Y, np.ones(N)))

        res = grid_search(X, Y)

        
        
---
