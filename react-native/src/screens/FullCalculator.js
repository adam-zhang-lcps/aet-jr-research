import React, { useState } from "react";
import { StyleSheet, View, Text, TouchableOpacity } from "react-native";

const Button = ({ title, onPress }) => {
  return (
    <TouchableOpacity onPress={onPress} style={styles.button}>
      <Text style={styles.buttonText}>{title}</Text>
    </TouchableOpacity>
  );
};

const FullCalculator = () => {
  const [value, setValue] = useState(0);
  const [prevValue, setPrevValue] = useState(0);
  const [operator, setOperator] = useState("+");

  const evaluate = () => {
    setPrevValue(eval(`${prevValue} ${operator} ${value}`));
    setValue(eval(`${prevValue} ${operator} ${value}`));
  };
  const number = (digit) => () => {
    setValue(value * 10 + digit);
  };
  const op = (op) => () => {
    evaluate();
    setValue(0);
    setOperator(op);
  };
  const clear = () => {
    setValue(0);
    setPrevValue(0);
    setOperator("+");
  };
  const equal = () => {
    evaluate();
    setPrevValue(0);
    setOperator("+");
  };

  return (
    <View style={styles.container}>
      <View style={styles.display}>
        <Text numberOfLines={1} style={styles.displayText}>
          {value}
        </Text>
      </View>
      <Button title="7" onPress={number(7)} />
      <Button title="8" onPress={number(8)} />
      <Button title="9" onPress={number(9)} />
      <Button title="+" onPress={op("+")} />
      <Button title="4" onPress={number(4)} />
      <Button title="5" onPress={number(5)} />
      <Button title="6" onPress={number(6)} />
      <Button title="-" onPress={op("-")} />
      <Button title="1" onPress={number(1)} />
      <Button title="2" onPress={number(2)} />
      <Button title="3" onPress={number(3)} />
      <Button title="*" onPress={op("*")} />
      <Button title="C" onPress={clear} />
      <Button title="0" onPress={number(0)} />
      <Button title="=" onPress={equal} />
      <Button title="/" onPress={op("/")} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    flexDirection: "row",
    flexWrap: "wrap",
    alignContent: "stretch",
  },
  display: {
    width: "100%",
    textAlign: "center",
    justifyContent: "center",
    alignItems: "center",
  },
  displayText: {
    fontSize: 64,
    textAlign: "center",
  },
  button: {
    width: "25%",
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 1,
  },
  buttonText: {
    fontSize: 40,
  },
});

export default FullCalculator;
