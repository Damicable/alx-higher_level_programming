#!/usr/bin/node
/**
 * This script prints the first argument passed to the console.
 */

// Get the first argument count (index 2 in process.argv)
const firstCount = process.argv[2];

// Check if the first argument exists and print it; otherwise, print "No argument"
if (firstCount) {
    console.log(firstCount);
} else {
    console.log("No argument");
}
