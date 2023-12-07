package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

var Time struct {
	hour int
}

func calcDistance(totalTime int, timeHeld int) int {
	return timeHeld * (totalTime - timeHeld)
}

func calcNumWaysToWin(totalTime int, distanceRecord int) int {
	wins := 0
	for i := 0; i < totalTime; i++ {
		if calcDistance(totalTime, i) > distanceRecord {
			wins++
		}
	}
	return wins
}

func main() {

	file, err := os.Open("p6-input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	f := bufio.NewReader(file)
	time, _, err := f.ReadLine()
	if err != nil {
		log.Fatal(err)
	}
	distance, _, err := f.ReadLine()
	if err != nil {
		log.Fatal(err)
	}

	regex := regexp.MustCompile("\\s+")
	var times, distances []string
	times = regex.Split(string(time), -1)[1:]
	distances = regex.Split(string(distance), -1)[1:]

	// Part 1
	numWaysToWin := 1
	for i := 0; i < len(times); i++ {
		totalTime, err := strconv.Atoi(times[i])
		if err != nil {
			log.Fatal(err)
		}
		distanceRecord, err := strconv.Atoi(distances[i])
		if err != nil {
			log.Fatal(err)
		}
		numWaysToWin *= calcNumWaysToWin(totalTime, distanceRecord)
	}
	fmt.Printf("number of ways to win product: %d\n", numWaysToWin)

	// Part 2
	totalTime := ""
	for i := 0; i < len(times); i++ {
		totalTime += times[i]
	}
	distanceRecord := ""
	for i := 0; i < len(distances); i++ {
		distanceRecord += distances[i]
	}
	tt, err := strconv.Atoi(totalTime)
	if err != nil {
		log.Fatal(err)
	}
	dr, err := strconv.Atoi(distanceRecord)
	if err != nil {
		log.Fatal(err)
	}
	numWaysToWinP2 := calcNumWaysToWin(tt, dr)

	fmt.Printf("number of ways to win product (P2): %d\n", numWaysToWinP2)
}
