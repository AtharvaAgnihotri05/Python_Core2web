
def outerFun():
    print("In Outer fun")

    def innerFun():
        print("inner fun")
    
    innerFun()

outerFun()

