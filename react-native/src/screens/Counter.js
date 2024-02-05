import React, { useState } from "react";
import { Text, StyleSheet, View, Button } from "react-native";

const Counter = () => {
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
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: "gray",
    justifyContent: "space-between",
    flex: 1,
  },
  buttonBlock: {
    backgroundColor: "gray",
    justifyContent: "space-evenly",
    flexDirection: "row",
    flex: 1,
  },
  countBlock: {
    backgroundColor: "black",
    flex: 15,
    justifyContent: "center",
  },
  countText: {
    color: "white",
    fontSize: 90,
    textAlign: "center",
  },
});

export default Counter;
