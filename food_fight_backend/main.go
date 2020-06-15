package main
import(
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	// "encoding/json"
)
type Restaurant struct {
	Name     string `json:"name"`
	Location string `json:"location"`
}
var restaurants []Restaurant

func getRestaurants(w http.ResponseWriter, r *http.Request){
	
}

func getAPIStatus(w http.ResponseWriter, r *http.Request){
	w.Write([]byte ("api is up and running\n"))
}

func main() {
	fmt.Printf("hello")
	restaurants = append(restaurants, Restaurant{Name: "Test", Location: "Irvine"})
	fmt.Println(restaurants)

	router := mux.NewRouter()
	router.HandleFunc("/restaurant", getRestaurants).Methods("GET")
	router.HandleFunc("/", getAPIStatus).Methods("GET")

	fmt.Println("router initialized")

	log.Fatal(http.ListenAndServe(":5000", router))
}
