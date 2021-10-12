package main

import (
	"io/ioutil"
	"net/http"
	"log"
	"fmt"
)

func main() {
	const ACE_URL string = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace";
	const API_KEY string = "ENavFdXno14bk22Nm45OF7RxuL8PpecM8ehvitSb"
	
	client := &http.Client{}
	
	ace_req, ace_err := http.NewRequest("GET", ACE_URL, nil)
	if ace_err != nil {
		log.Fatalln("error 1", ace_err)
	}
	ace_req.Header.Set("x-api-key", API_KEY)
	
	ace_resp, ace_err := client.Do(ace_req)
	if ace_err != nil {
		log.Fatalln("error 2", ace_err)
	}
	ace_b, ace_err := ioutil.ReadAll(ace_resp.Body)
	if ace_err != nil {
		log.Fatalln("error 3", ace_err)
	}
	fmt.Println(ace_b)
	return
}