package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Hand struct {
	Cards string
	Bid   int
}

func (h Hand) FiveOfAKind() bool {
	numJokers := strings.Count(h.Cards, "J")
	if numJokers == 5 {
		return true
	}
	for _, c := range h.Cards {
		if c == 'J' {
			continue
		}
		if strings.Count(h.Cards, string(c))+numJokers == 5 {
			return true
		}
	}
	return false
}

func (h Hand) FourOfAKind() bool {
	numJokers := strings.Count(h.Cards, "J")
	for _, c := range h.Cards {
		if c == 'J' {
			continue
		}
		if strings.Count(h.Cards, string(c))+numJokers == 4 {
			return true
		}
	}
	return false
}

func (h Hand) FullHouse() bool {
	numJokers := strings.Count(h.Cards, "J")
	if h.FourOfAKind() {
		return true
	}

	for _, c := range h.Cards {
		if c == 'J' {
			continue
		}
		if strings.Count(h.Cards, string(c))+numJokers == 3 {
			for _, d := range h.Cards {
				if c == d || d == 'J' {
					continue
				}
				if strings.Count(h.Cards, string(d)) == 2 {
					return true
				}
			}
		} else if strings.Count(h.Cards, string(c))+numJokers == 2 {
			for _, d := range h.Cards {
				if c == d || d == 'J' {
					continue
				}
				if strings.Count(h.Cards, string(d)) == 3 {
					return true
				}
			}
		}
	}
	return false
}

func (h Hand) ThreeOfAKind() bool {
	numJokers := strings.Count(h.Cards, "J")
	for _, c := range h.Cards {
		if c == 'J' {
			continue
		}
		if strings.Count(h.Cards, string(c))+numJokers >= 3 {
			return true
		}
	}
	return false
}

func (h Hand) TwoPairs() bool {
	numJokers := strings.Count(h.Cards, "J")
	if numJokers >= 2 || h.ThreeOfAKind() {
		return true
	}
	for _, c := range h.Cards {
		if strings.Count(h.Cards, string(c)) >= 2 {
			for _, d := range h.Cards {
				if c == d || d == 'J' {
					continue
				}
				if strings.Count(h.Cards, string(d))+numJokers >= 2 {
					return true
				}
			}
		} else if strings.Count(h.Cards, string(c))+numJokers >= 2 {
			for _, d := range h.Cards {
				if c == d || d == 'J' {
					continue
				}
				if strings.Count(h.Cards, string(d)) >= 2 {
					return true
				}
			}
		}
	}
	return false
}

func (h Hand) OnePair() bool {
	pairs := 0
	foundPair1 := ""
	if strings.Count(h.Cards, "J") >= 1 || h.TwoPairs() {
		return true
	}
	for _, c := range h.Cards {
		if string(c) == foundPair1 {
			continue
		}
		if strings.Count(h.Cards, string(c)) == 2 {
			foundPair1 = string(c)
			pairs++
		}
	}
	return pairs == 1
}

func (h Hand) HighCard() bool {
	for _, c := range h.Cards {
		if strings.Count(h.Cards, string(c)) != 1 {
			return false
		}
	}
	return true
}

func compareHands(a Hand, b Hand) bool {
	if a.FiveOfAKind() && !b.FiveOfAKind() {
		return true
	} else if !a.FiveOfAKind() && b.FiveOfAKind() {
		return false
	} else if a.FourOfAKind() && !b.FourOfAKind() {
		return true
	} else if !a.FourOfAKind() && b.FourOfAKind() {
		return false
	} else if a.FullHouse() && !b.FullHouse() {
		return true
	} else if !a.FullHouse() && b.FullHouse() {
		return false
	} else if a.ThreeOfAKind() && !b.ThreeOfAKind() {
		return true
	} else if !a.ThreeOfAKind() && b.ThreeOfAKind() {
		return false
	} else if a.TwoPairs() && !b.TwoPairs() {
		return true
	} else if !a.TwoPairs() && b.TwoPairs() {
		return false
	} else if a.OnePair() && !b.OnePair() {
		return true
	} else if !a.OnePair() && b.OnePair() {
		return false
	}
	royalCards := map[string]int{
		"A": 14,
		"K": 13,
		"Q": 12,
		"J": 0, // Joker
		"T": 10,
	}
	for i := 0; i < len(a.Cards); i++ {
		if a.Cards[i] != b.Cards[i] {
			aCard, err := strconv.Atoi(string(a.Cards[i]))
			if err != nil {
				aCard = royalCards[string(a.Cards[i])]
			}
			bCard, err := strconv.Atoi(string(b.Cards[i]))
			if err != nil {
				bCard = royalCards[string(b.Cards[i])]
			}
			return aCard > bCard
		}
	}
	return false
}

func sortHands(hands []Hand) []Hand {
	for i := 0; i < len(hands); i++ {
		for j := 0; j < len(hands)-1; j++ {
			if compareHands(hands[j], hands[j+1]) {
				hands[j], hands[j+1] = hands[j+1], hands[j]
			}
		}
	}
	return hands
}

func calcTotalWinnings(hands []Hand) int {
	totalWinnings := 0
	for i := 0; i < len(hands); i++ {
		totalWinnings += hands[i].Bid * (i + 1)
	}
	return totalWinnings
}

func main() {

	file, err := os.Open("p7-input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var hands []Hand
	regex := regexp.MustCompile(`\s+`)
	f := bufio.NewScanner(file)
	for f.Scan() {
		line := f.Text()
		cards := regex.Split(line, -1)[0]
		bid, err := strconv.Atoi(regex.Split(line, -1)[1])
		if err != nil {
			log.Fatal(err)
		}
		hand := Hand{cards, bid}
		hands = append(hands, hand)
	}
	hands = sortHands(hands)
	for i := 0; i < len(hands); i++ {
		fmt.Printf("rank: %d: hand: %s bid: %d\n", i+1, hands[i].Cards, hands[i].Bid)
	}
	fmt.Printf("Total winnings: %d\n", calcTotalWinnings(hands))
}
