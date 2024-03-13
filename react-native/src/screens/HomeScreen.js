import React from "react";
import { View, Text, StyleSheet, TouchableOpacity, Image } from "react-native";

const NavigationButton = ({ screen, navigate }) => {
  return (
    <TouchableOpacity onPress={() => navigate(screen)}>
      <Text
        style={{
          fontSize: 24,
          color: "blue",
        }}
      >
        Go to {screen}
      </Text>
    </TouchableOpacity>
  );
};

const HomeScreen = (props) => {
  const { navigation } = props;
  return (
    <View>
      <Text style={styles.text}>HomeScreen</Text>
      <Text style={styles.text}>Hi there!</Text>
      <View
        style={{
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        {[
          "SongListScreen",
          "Counter",
          "StylingBoxScreen",
          "NorwayFlag",
          "ThePredictor",
          "ImageScreen",
          "Counters",
          "SimpleCalculator",
          "FullCalculator",
          "FoodieScreen",
        ].map((s, i) => (
          <NavigationButton screen={s} navigate={navigation.navigate} key={i} />
        ))}
        <TouchableOpacity onPress={() => navigation.navigate("CuteScreen")}>
          <Image
            style={{
              height: 300,
              width: 400,
            }}
            source={{ uri: "http://d23dyxeqlo5psv.cloudfront.net/cat.gif" }}
          />
          <Text
            style={{
              alignSelf: "center",
            }}
          >
            Go to CuteScreen
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
});

export default HomeScreen;
