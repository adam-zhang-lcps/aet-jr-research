import React, { useState } from "react";
import { Text, StyleSheet, View, Button, TouchableOpacity } from "react-native";

const Counter = ({ navigation }) => {
  const [count, setCount] = useState(0);

  return (
    <View style={styles.container}>
      <View style={styles.buttonBlock}>
        <Button onPress={() => setCount(count + 1)} title="Increment" />
        <Button onPress={() => setCount(count - 1)} title="Decrement" />
      </View>
      <View style={styles.countBlock}>
        <Text style={styles.countText}>{count}</Text>
      </View>
      <View style={styles.buttonBlock}>
        <Button onPress={() => setCount(0)} title="Reset" />
      </View>
      <TouchableOpacity
        onPress={() => navigation.navigate("Home")}
        style={{
          flexGrow: 1,
        }}
      >
        <Text
          style={{
            alignSelf: "center",
            fontSize: 24,
          }}
        >
          Return Home
        </Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: "gray",
    justifyContent: "space-between",
    flexGrow: 1,
  },
  buttonBlock: {
    backgroundColor: "gray",
    justifyContent: "space-evenly",
    flexDirection: "row",
    flexGrow: 1,
  },
  countBlock: {
    backgroundColor: "black",
    flexGrow: 20,
    justifyContent: "center",
  },
  countText: {
    color: "white",
    fontSize: 90,
    textAlign: "center",
  },
});

export default Counter;
