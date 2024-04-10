#!/usr/bin/node
let counter=0;
if (process.argv[2]==undefined||isNaN(process.argv[2]))
    console.log("Missing number of occurrences");
else
{
    counter=process.argv[2];
    let mySents="C is fun";
    for (let i=0;i<counter;i++)
    {
        console.log(mySents);

    }
}