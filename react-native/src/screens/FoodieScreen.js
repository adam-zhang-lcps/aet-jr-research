import React, { useState } from "react";
import { Text, StyleSheet, View, Button } from "react-native";
import SearchBar from "../components/SearchBar";
import yelp from "../api/yelp";

const FoodieScreen = ({ navigation }) => {
  const [term, setTerm] = useState("");
  const [results, setResults] = useState([]);
  const [errMessage, setErrMessage] = useState("");

  const makeYelpRequest = async () => {
    try {
      const response = await yelp.get("/search", {
        params: {
          limit: 20,
          term: "asian",
          location: "leesburg va",
        },
      });

      console.log(response.data.businesses);

      setResults(response.data.businesses);
    } catch (err) {
      console.log(err);
      setErrMessage("Something went wrong");
    }
  };

  return (
    <View>
      {errMessage ? <Text>{errMessage}</Text> : null}
      <SearchBar
        term={term}
        onTermChange={setTerm}
        onTermSubmit={makeYelpRequest}
      />
      <Text styles={styles.text}>this is the foodie screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
});

export default FoodieScreen;
