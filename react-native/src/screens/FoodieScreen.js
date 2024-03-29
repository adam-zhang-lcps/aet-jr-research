import React, { useEffect, useState } from "react";
import { Text, StyleSheet, View, FlatList, ScrollView } from "react-native";
import SearchBar from "../components/SearchBar";
import yelp from "../api/yelp";
import YelpBusinessPreview from "../components/YelpBusinessPreview";

const ScrollableRow = ({ title, businesses, navigation }) => {
  return (
    <View style={styles.rowContainer}>
      <Text style={styles.rowTitle}>{title}</Text>
      <FlatList
        horizontal
        data={businesses}
        keyExtractor={(result) => result.id}
        renderItem={({ item }) => {
          return (
            <YelpBusinessPreview business={item} navigation={navigation} />
          );
        }}
      />
    </View>
  );
};

const FoodieScreen = ({ navigation }) => {
  const [searchResults, setSearchResults] = useState([]);
  const [costEffective, setCostEffective] = useState("");
  const [moreExpensive, setMoreExpensive] = useState("");
  const [asian, setAsian] = useState("");
  const [errMessage, setErrMessage] = useState("");

  const makeYelpRequest = async (params, set) => {
    setErrMessage(null);

    try {
      const response = await yelp.get("/search", {
        params: {
          limit: 20,
          location: "leesburg va",
          ...params,
        },
      });

      set(response.data.businesses);
    } catch (err) {
      console.error(err);
      setErrMessage("Something went wrong");
    }
  };

  // What the f*cking hell, React?
  // This is the recommended way to fetch data on component mount with async/await
  useEffect(() => {
    (async () => {
      await Promise.all([
        makeYelpRequest({ price: 1 }, setCostEffective),
        makeYelpRequest({ price: "3,4" }, setMoreExpensive),
        makeYelpRequest({ term: "asian" }, setAsian),
      ]);
    })();
  }, []);

  const onSearch = async (term) => {
    await makeYelpRequest({ term }, setSearchResults);
  };

  return (
    <View style={styles.container}>
      {errMessage ? <Text>{errMessage}</Text> : null}
      <SearchBar onSubmit={onSearch} />
      {searchResults.length > 0 ? (
        <FlatList
          data={searchResults}
          keyExtractor={(result) => result.id}
          renderItem={({ item }) => {
            return (
              <YelpBusinessPreview business={item} navigation={navigation} />
            );
          }}
        />
      ) : (
        <ScrollView>
          <ScrollableRow
            title="Cost Effective"
            businesses={costEffective}
            navigation={navigation}
          />
          <ScrollableRow
            title="More Expensive"
            businesses={moreExpensive}
            navigation={navigation}
          />
          <ScrollableRow
            title="Asian"
            businesses={asian}
            navigation={navigation}
          />
        </ScrollView>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column",
    backgroundColor: "#fff",
  },
  text: {
    fontSize: 30,
  },
  rowContainer: {
    marginVertical: 10,
  },
  rowTitle: {
    fontSize: 28,
    fontWeight: "bold",
    marginLeft: 15,
  },
});

export default FoodieScreen;
