import React from "react";
import { Text, StyleSheet, View, Image } from "react-native";

/*
 * functional component: CuteAnimals
 *
 * note: how the variable, messageStr, is accessed within the Text component
 *       how style objects are defined within the StyleSheet component
 *       Text attributes reference: https://reactnative.dev/docs/text-style-props
 */
const CuteAnimals = () => {
    /*
     * block comment - like Java
     */
    // line comments - like Java

    //defining a variable
    const messageStr = "My Cat, Precious";

    return (
        <View>
            <Text style={styles.titleText}>Cute Animals</Text>
            <Image
                style={styles.image}
                source={{ uri: "http://d23dyxeqlo5psv.cloudfront.net/cat.gif" }}
            />
            <Text style={styles.messageText}> {messageStr} </Text>
        </View>
    );
};

const styles = StyleSheet.create({
    titleText: {
        backgroundColor: "honeydew",
        fontSize: 40,
        color: "indigo",
        fontFamily: "monospace",
        textAlign: "center",
    },
    image: {
        height: 300,
        width: 400,
    },
    messageText: {
        backgroundColor: "#000000",
        fontSize: 35,
        color: "#ffffff",
        fontWeight: "bold",
    },
});

export default CuteAnimals;
