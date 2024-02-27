import React, { useState } from "react";
import { View, StyleSheet, Text, TextInput } from "react-native";

const SimpleCalculator = () => {
  const [number1, setNumber1] = useState(0);
  const [number2, setNumber2] = useState(0);
  const [result, setResult] = useState(0);
  const [operation, setOperation] = useState("+");

  const calculate = (operation) => {
    setOperation(operation);
    setResult(eval(`${number1} ${operation} ${number2}`));
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Simple Calculator</Text>
      <View style={styles.inputContainer}>
        <TextInput
          keyboardType="numeric"
          onChangeText={setNumber1}
          value={number1.toString()}
          style={styles.input}
        />
        <Text style={styles.operation}> {operation} </Text>
        <TextInput
          keyboardType="numeric"
          onChangeText={setNumber2}
          value={number2.toString()}
          style={styles.input}
        />
      </View>
      <Text style={styles.answer}>Answer: {result}</Text>
      <Text style={styles.instructions}>Press a button below to calculate</Text>
      <View style={styles.buttonsContainer}>
        <Text style={styles.button} onPress={() => calculate("+")}>
          +
        </Text>
        <Text style={styles.button} onPress={() => calculate("-")}>
          -
        </Text>
        <Text style={styles.button} onPress={() => calculate("*")}>
          *
        </Text>
        <Text style={styles.button} onPress={() => calculate("/")}>
          /
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "column",
  },
  title: {
    fontSize: 36,
    textAlign: "center",
  },
  inputContainer: {
    flexBasis: 80,
    flexDirection: "row",
  },
  input: {
    flex: 1,
    borderColor: "gray",
    borderWidth: 1,
    margin: 10,
    padding: 10,
    fontSize: 24,
  },
  operation: {
    fontSize: 36,
    alignSelf: "center",
  },
  answer: {
    fontSize: 36,
    textAlign: "center",
  },
  instructions: {
    fontSize: 24,
    textAlign: "center",
  },
  buttonsContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
  },
  button: {
    width: "40%",
    fontSize: 36,
    textAlign: "center",
    borderWidth: 1,
    borderColor: "black",
    padding: 10,
    marginTop: 10,
    marginLeft: "5%",
    marginRight: "5%",
  },
});

export default SimpleCalculator;
