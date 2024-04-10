#!/usr/bin/node
let counter=0;
if (process.argv[2]!=undefined)
    counter=process.argv[2];
let mySents="C is fun";
for (let i=0;i<counter;i++)
{
    console.log(mySents);

}