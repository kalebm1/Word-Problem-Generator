# Word Problem Generator
This Python script generate random word problems of varying difficulty and type.

There are a few different ways you can use this generator.

## Step 1: Import wordProblem file
You must first import the word problem script into your project:
```
>>from wordProblem import wordProblem
```

## Step 2: Create a wordProblem object
You must then create a variable that holds a wordProblem object.
```
>>problem = wordProblem()
```

## Step 3: Generate Problem
Once you have a wordProblem object, you must generate the data to
go inside the word problem. You can do this by setting each value
yourself, or by simply calling randomizeProblem()
```
>>problem.setGender("male")
>>problem.setName("Kaleb")
>>problem.setDif("easy")
>>OR
>>problem.randomizeProblem()
```

## Step 4: Print the problem out
Now that you have the data inside the wordProblem object,
you are now ready to display the generated word problem.
to do that, simply use the following command:
```
>>print(problem.buildWordProblem())
```

## Step 5: Get the Answer
To get the answer for your new word problem, use the following
command:
```
>>print("Answer = "+str(problem.getAnswer()))
```

# TODO:
- [ ] Make a GUI for the program...
