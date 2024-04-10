#!/usr/bin/node
let counter=0;
if (process.argv[2]==undefined||isNaN(process.argv[2]))
    console.log("Missing size");
else
{
    counter=process.argv[2];
    for (let j=0;j<counter;j++)
    {
       
        
            console.log("X".repeat(counter));

        
    }
}