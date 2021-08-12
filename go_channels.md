Go channels: Use cases and tutorial

A channel is a communication mechanism that allows goroutines to exchange data, among other things.

Go channels usages:
- Use Channels as Futures/Promises

  — Futures and promises are used in many other popular languages. They are     often associated with requests and responses.
  

- Use Channels for Notifications

  — Notifications can be thought of as one-of-a-kind requests/responses in which   the values returned are unimportant. We usually use the blank struct type struct   as the notification channel element types because the size of type struct is zero,   therefore the values of struct don't consume memory.
  

- Use Channels as Counting Semaphores

  — To impose a maximum number of concurrent requests, counting semaphores  are frequently utilised.  There are two ways to obtain one piece of ownership of  a channel semaphore, similar to how channels can be used as mutexes.    Ownership is acquired with a send, and it is released through a receive.  Take
 possession with a receive and release it with a send.

There are some specific rules. Firstly, each channel allows the exchange of a particular data type, which is also called the element type of the channel, and secondly, for a channel to operate properly, you will need someone to receive what is sent via the channel. 

You should declare a new channel using the chan keyword, and you can close a channel using the close() function.

Finally, a very important detail: when you are using a channel as a function parameter, you can specify its direction; that is, whether it is going to be used for sending or receiving. 

If you know the purpose of a channel in advance, you should use this capability because it will make your programs more robust, as well as safer.

You will not be able to send data accidentally to a channel from which you should only receive data, or receive data from a channel to which you should only be sending data. 

As a result, if you declare that a channel function parameter will be used for reading only and you try to write to it, you will get an error message that will most likely save you from nasty bugs.


Writing to a channel 

The code in this subsection will teach you how to write to a channel. Writing the value x to channel c is as easy as writing c <- x . 

The arrow shows the direction of the value, and you will have no problem with this statement as long as both x and c have the same type. 

The example code in this section is saved in writeCh.go , and it will be presented in three parts. 

The first code segment from writeCh.go is as follows:


    package main
    import (
      "fmt"
      "time"
    )
    
    func writeToChannel(c chan int, x int) {
       fmt.Println(x)
       c <- x
       close(c)
       fmt.Println(x)
    }

The chan keyword is used for declaring that the c function parameter will be a channel, and it should be followed by the type of the channel ( int ). 

The c <- x statement allows you to write the value x to channel c , and the close() function closes the channel. 

The second part of writeCh.go contains the following Go code:


    func main() {
        c := make(chan int)


The remaining code from writeCh.go is as follows:


     go writeToChannel(c, 10)
     time.Sleep(1 * time.Second)
    }

Here, you execute the writeToChannel() function as a goroutine and call time.Sleep() in order to give enough time to the writeToChannel() function to execute.

Executing writeCh.go will create the following output:


    $ go run writeCh.go
    10

The strange thing here is that the writeToChannel() function prints the given value only once. 

The cause of this unexpected output is that the second fmt.Println(x) statement is never executed. The reason for this is pretty simple once you understand how channels work: the c <- x statement is blocking the execution of the rest of the writeToChannel() function because nobody is reading what was written to the c channel. 

Therefore, when the time.Sleep(1 * time.Second) statement finishes, the program terminates without waiting for writeToChannel() .

The next section will illustrate how to read data from a channel.


Reading from a channel

In this section, you will learn how to read from a channel. You can read a single value from a channel named c by executing <-c . In this case, the direction is from the channel to the outer world.

The name of the program that will be used to help you understand how to read from a channel is readCh.go , and it will be presented in three parts.

The first code segment from readCh.go is shown in the following Go code:


    package main
    import (
    "fmt"
    "time"
    )
    
    func writeToChannel(c chan int, x int) {
      fmt.Println("1", x)
      c <- x
      close(c)
      fmt.Println("2", x)
    }

The implementation of the writeToChannel() function is the same as before.

The second part of readCh.go follows:


    func main() {
      c := make(chan int)
      go writeToChannel(c, 10)
      time.Sleep(1 * time.Second)
      fmt.Println("Read:", <-c)
      time.Sleep(1 * time.Second)

In the preceding code, you read from channel c using the <-c notation. If you want to store that value to a variable named k instead of just printing it, you can use a k := <-c statement. 

The second time.Sleep(1 * time.Second) statement gives you the time to read from the channel.

The last code portion of readCh.go contains the following Go code:


    _, ok := <-c
    
    if ok {
      fmt.Println("Channel is open!")
     } else {
      fmt.Println("Channel is closed!")
     }
    }

In the preceding code, you can see a technique for determining whether a given channel is open or not. 

The current Go code works fine when the channel is closed; however, if the channel was open, the Go code presented here would have discarded the read value of the channel because of the use of the _ character in the _, ok := <-c statement.

Use a proper variable name instead of _ if you also want to store the value found in the channel in case it is open.

Executing readCh.go will generate the following output:


    $ go run readCh.go
    1 10
    Read: 10
    2 10
    Channel is closed!
    $ go run readCh.go
    1 10
    2 10
    Read: 10
    Channel is closed!

Although the output is still not deterministic, both the fmt.Println(x) statements of the writeToChannel() function are executed because the channel is unblocked when you read from it.


Receiving from a closed channel

In this subsection, you will learn what happens when you try to read from a closed channel using the Go code found in readClose.go , which is going to be presented in two parts.

The first part of readClose.go is as follows:


    package main
    import (
    "fmt"
    )
    
    func main() {
      willClose := make(chan int, 10)
      willClose <- -1
      willClose <- 0
      willClose <- 2
      <-willClose
      <-willClose
      <-willClose
    

In this part of the program, we create a new int channel named willClose , we write data to it, and we read all that data without doing anything with it.

The second part of readClose.go contains the following code:


      close(willClose)
      read := <-willClose
      fmt.Println(read)
    }

In this part, we close the willClose channel and we try to read from the willClose channel, which we emptied in the previous part.

Executing readClose.go will generate the following output:


    $ go run readClose.go
    0

This means that reading from a closed channel returns the zero value of its data type, which in this case is 0 .


Channels as function parameters

Although neither readCh.go nor writeCh.go used this feature, Go allows you to specify the direction of a channel when used as a function parameter; that is, whether it will be used for reading or writing. 

These two types of channels are called unidirectional channels, whereas, by default, channels are bidirectional.

Examine the Go code of the following two functions:


    func f1(c chan int, x int) {
     fmt.Println(x)
     c <- x
    }
    
    func f2(c chan<- int, x int) {
     fmt.Println(x)
     c <- x
    }

Although both functions implement the same functionality, their definitions are slightly different. The difference is created by the <- symbol found on the right of the chan keyword in the definition of the f2() function. 

This denotes that the c channel can be used for writing only. If the code of a Go function attempts to read from a write-only channel (send-only channel) parameter, the Go compiler will generate the following kind of error message:


    # command-line-arguments
    a.go:19:11: invalid operation: range in (receive from send-only type chan<-int)

Similarly, you can have the following function definitions:


    func f1(out chan<- int64, in <-chan int64) {
      fmt.Println(x)
      c <- x
    }
    
    func f2(out chan int64, in chan int64) {
      fmt.Println(x)
      c <- x
    }

The definition of f2() combines a read-only channel named in with a write-only channel named out .  If you accidentally try to write and close a read-only channel (receive-only channel) parameter of a function, you will get the following kind of error message:


    # command-line-arguments
    a.go:13:7: invalid operation: out <- i (send to receive-only type <-chan int)
    a.go:15:7: invalid operation: close(out) (cannot close receive-only 
    channel)


Range over channels

We can use range syntax in Golang to iterate over a channel to read its values. 


    package main
    
    import "fmt"
    
    func main() {
    
        ch := make(chan string, 2)
        ch <- "one"
        ch <- "two"
        close(ch)
    
        for elem := range ch {
            fmt.Println(elem)
        }
    }

Executing the previous code outputs: 


    $ go run range-over-channels.go
    one
    two


Conclusion

Channels are used for communicating between concurrently running functions by sending and receiving data of a specific element type. When you have numerous goroutines running at the same time, channels are the most convenient way for them to communicate with one another.

Thanks for reading, happy coding 🙂 


