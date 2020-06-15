package main
import(
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"	
	"io/ioutil"
	"strconv"
	"encoding/json"
)
type Restaurant struct {
	Name     string `json:"name"`
	Location string `json:"location"`
}
var restaurants []Restaurant
var api_key = "x4boCEjaccL6otSoUD7vMepPyljMPDyQLY25d-tGqO4niXHY02orCyyHhErrFdJ6daaMXZJJ0PqTCnDlu373YWsXbzWJGTgnp8gqZkS-CJcqpsbQiXV-ZEegvu01W3Yx"
var BASE_URL = "https://api.yelp.com/v3/"
func getRestaurants(w http.ResponseWriter, r *http.Request){
	
}

func searchResults(location string, limit int){
	API_URL := BASE_URL + "businesses/search"
	bearer := "Bearer " + api_key
	req, err := http.NewRequest(http.MethodGet, API_URL, nil)
	req.Header.Set("Authorization", bearer)
	req.Header.Add("Accept", "application/json")
	if err != nil{
		log.Fatalln(err)
	}
	q := req.URL.Query()
	q.Add("location", location)
	q.Add("limit", strconv.Itoa(limit))
	req.URL.RawQuery = q.Encode()
	fmt.Println(req.URL.String())

	client := http.DefaultClient
	resp, err := client.Do(req)
	if err != nil {
		log.Fatalln(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil{
		log.Fatalln(err)
	}
	fmt.Printf("%v\n", string([]byte(body)))
	var m map[string]interface{}
	json.Unmarshal(body, &m)
	businesses := m["businesses"].([]interface{})
	// TODO -> create structs to unmarshal the JSON objects
	for key, value := range businesses {
		fmt.Println(key, value)
	}
}

func getAPIStatus(w http.ResponseWriter, r *http.Request){
	w.Write([]byte ("api is up and running\n"))
}

func main() {
	fmt.Printf("hello")
	restaurants = append(restaurants, Restaurant{Name: "Test", Location: "Irvine"})
	fmt.Println(restaurants)
	searchResults("Irvine", 5)

	router := mux.NewRouter()
	router.HandleFunc("/restaurant", getRestaurants).Methods("GET")
	router.HandleFunc("/", getAPIStatus).Methods("GET")

	fmt.Println("router initialized")
	log.Fatal(http.ListenAndServe(":5001", router))
}
