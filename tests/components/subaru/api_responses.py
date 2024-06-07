"""Sample API response data for tests."""

from datetime import UTC, datetime

from homeassistant.components.subaru.const import (
    API_GEN_1,
    API_GEN_2,
    API_GEN_3,
    VEHICLE_API_GEN,
    VEHICLE_HAS_EV,
    VEHICLE_HAS_REMOTE_SERVICE,
    VEHICLE_HAS_REMOTE_START,
    VEHICLE_HAS_SAFETY_SERVICE,
    VEHICLE_MODEL_NAME,
    VEHICLE_MODEL_YEAR,
    VEHICLE_NAME,
    VEHICLE_STATUS,
    VEHICLE_VIN,
)

TEST_VIN_1_G1 = "JF2ABCDE6L0000001"
TEST_VIN_2_EV = "JF2ABCDE6L0000002"
TEST_VIN_3_G3 = "JF2ABCDE6L0000003"

VEHICLE_DATA = {
    TEST_VIN_1_G1: {
        VEHICLE_VIN: TEST_VIN_1_G1,
        VEHICLE_MODEL_YEAR: "2017",
        VEHICLE_MODEL_NAME: "Outback",
        VEHICLE_NAME: "test_vehicle_1",
        VEHICLE_HAS_EV: False,
        VEHICLE_API_GEN: API_GEN_1,
        VEHICLE_HAS_REMOTE_START: True,
        VEHICLE_HAS_REMOTE_SERVICE: True,
        VEHICLE_HAS_SAFETY_SERVICE: False,
    },
    TEST_VIN_2_EV: {
        VEHICLE_VIN: TEST_VIN_2_EV,
        VEHICLE_MODEL_YEAR: "2019",
        VEHICLE_MODEL_NAME: "Crosstrek",
        VEHICLE_NAME: "test_vehicle_2",
        VEHICLE_HAS_EV: True,
        VEHICLE_API_GEN: API_GEN_2,
        VEHICLE_HAS_REMOTE_START: True,
        VEHICLE_HAS_REMOTE_SERVICE: True,
        VEHICLE_HAS_SAFETY_SERVICE: True,
    },
    TEST_VIN_3_G3: {
        VEHICLE_VIN: TEST_VIN_3_G3,
        VEHICLE_MODEL_YEAR: "2022",
        VEHICLE_MODEL_NAME: "Ascent",
        VEHICLE_NAME: "test_vehicle_3",
        VEHICLE_HAS_EV: False,
        VEHICLE_API_GEN: API_GEN_3,
        VEHICLE_HAS_REMOTE_START: True,
        VEHICLE_HAS_REMOTE_SERVICE: True,
        VEHICLE_HAS_SAFETY_SERVICE: True,
    },
}

MOCK_DATETIME = datetime.fromtimestamp(1595560000, UTC)

VEHICLE_STATUS_EV = {
    VEHICLE_STATUS: {
        "AVG_FUEL_CONSUMPTION": 51.1,
        "DISTANCE_TO_EMPTY_FUEL": 170,
        "DOOR_BOOT_POSITION": "CLOSED",
        "DOOR_ENGINE_HOOD_POSITION": "CLOSED",
        "DOOR_FRONT_LEFT_POSITION": "CLOSED",
        "DOOR_FRONT_RIGHT_POSITION": "CLOSED",
        "DOOR_REAR_LEFT_POSITION": "CLOSED",
        "DOOR_REAR_RIGHT_POSITION": "CLOSED",
        "EV_CHARGER_STATE_TYPE": "CHARGING",
        "EV_CHARGE_SETTING_AMPERE_TYPE": "MAXIMUM",
        "EV_CHARGE_VOLT_TYPE": "CHARGE_LEVEL_1",
        "EV_DISTANCE_TO_EMPTY": 1,
        "EV_IS_PLUGGED_IN": "UNLOCKED_CONNECTED",
        "EV_STATE_OF_CHARGE_MODE": "EV_MODE",
        "EV_STATE_OF_CHARGE_PERCENT": 20,
        "EV_TIME_TO_FULLY_CHARGED_UTC": MOCK_DATETIME,
        "ODOMETER": 1234,
        "TIMESTAMP": 1595560000.0,
        "TRANSMISSION_MODE": "UNKNOWN",
        "TYRE_PRESSURE_FRONT_LEFT": 0.0,
        "TYRE_PRESSURE_FRONT_RIGHT": 31.9,
        "TYRE_PRESSURE_REAR_LEFT": 32.6,
        "TYRE_PRESSURE_REAR_RIGHT": None,
        "VEHICLE_STATE_TYPE": "IGNITION_OFF",
        "WINDOW_BACK_STATUS": "UNKNOWN",
        "WINDOW_FRONT_LEFT_STATUS": "VENTED",
        "WINDOW_FRONT_RIGHT_STATUS": "VENTED",
        "WINDOW_REAR_LEFT_STATUS": "UNKNOWN",
        "WINDOW_REAR_RIGHT_STATUS": "UNKNOWN",
        "WINDOW_SUNROOF_STATUS": "UNKNOWN",
        "LATITUDE": 40.0,
        "LONGITUDE": -100.0,
    }
}


VEHICLE_STATUS_G3 = {
    VEHICLE_STATUS: {
        "AVG_FUEL_CONSUMPTION": 51.1,
        "DISTANCE_TO_EMPTY_FUEL": 170,
        "DOOR_BOOT_POSITION": "CLOSED",
        "DOOR_ENGINE_HOOD_POSITION": "CLOSED",
        "DOOR_FRONT_LEFT_POSITION": "CLOSED",
        "DOOR_FRONT_RIGHT_POSITION": "CLOSED",
        "DOOR_REAR_LEFT_POSITION": "CLOSED",
        "DOOR_REAR_RIGHT_POSITION": "CLOSED",
        "REMAINING_FUEL_PERCENT": 77,
        "ODOMETER": 1234,
        "TIMESTAMP": 1595560000.0,
        "TRANSMISSION_MODE": "UNKNOWN",
        "TYRE_PRESSURE_FRONT_LEFT": 0.0,
        "TYRE_PRESSURE_FRONT_RIGHT": 31.9,
        "TYRE_PRESSURE_REAR_LEFT": 32.6,
        "TYRE_PRESSURE_REAR_RIGHT": None,
        "VEHICLE_STATE_TYPE": "IGNITION_OFF",
        "WINDOW_BACK_STATUS": "UNKNOWN",
        "WINDOW_FRONT_LEFT_STATUS": "VENTED",
        "WINDOW_FRONT_RIGHT_STATUS": "VENTED",
        "WINDOW_REAR_LEFT_STATUS": "UNKNOWN",
        "WINDOW_REAR_RIGHT_STATUS": "UNKNOWN",
        "WINDOW_SUNROOF_STATUS": "UNKNOWN",
        "LATITUDE": 40.0,
        "LONGITUDE": -100.0,
    }
}

EXPECTED_STATE_EV_IMPERIAL = {
    "AVG_FUEL_CONSUMPTION": "51.1",
    "DISTANCE_TO_EMPTY_FUEL": "170",
    "EV_CHARGER_STATE_TYPE": "CHARGING",
    "EV_CHARGE_SETTING_AMPERE_TYPE": "MAXIMUM",
    "EV_CHARGE_VOLT_TYPE": "CHARGE_LEVEL_1",
    "EV_DISTANCE_TO_EMPTY": "1",
    "EV_IS_PLUGGED_IN": "UNLOCKED_CONNECTED",
    "EV_STATE_OF_CHARGE_MODE": "EV_MODE",
    "EV_STATE_OF_CHARGE_PERCENT": "20",
    "EV_TIME_TO_FULLY_CHARGED_UTC": "2020-07-24T03:06:40+00:00",
    "ODOMETER": "1234",
    "TIMESTAMP": 1595560000.0,
    "TRANSMISSION_MODE": "UNKNOWN",
    "TYRE_PRESSURE_FRONT_LEFT": "0.0",
    "TYRE_PRESSURE_FRONT_RIGHT": "31.9",
    "TYRE_PRESSURE_REAR_LEFT": "32.6",
    "TYRE_PRESSURE_REAR_RIGHT": "unknown",
    "VEHICLE_STATE_TYPE": "IGNITION_OFF",
    "LATITUDE": 40.0,
    "LONGITUDE": -100.0,
}

EXPECTED_STATE_EV_METRIC = {
    "AVG_FUEL_CONSUMPTION": "4.6",
    "DISTANCE_TO_EMPTY_FUEL": "274",
    "EV_CHARGER_STATE_TYPE": "CHARGING",
    "EV_CHARGE_SETTING_AMPERE_TYPE": "MAXIMUM",
    "EV_CHARGE_VOLT_TYPE": "CHARGE_LEVEL_1",
    "EV_DISTANCE_TO_EMPTY": "2",
    "EV_IS_PLUGGED_IN": "UNLOCKED_CONNECTED",
    "EV_STATE_OF_CHARGE_MODE": "EV_MODE",
    "EV_STATE_OF_CHARGE_PERCENT": "20",
    "EV_TIME_TO_FULLY_CHARGED_UTC": "2020-07-24T03:06:40+00:00",
    "ODOMETER": "1986",
    "TIMESTAMP": 1595560000.0,
    "TRANSMISSION_MODE": "UNKNOWN",
    "TYRE_PRESSURE_FRONT_LEFT": "0.0",
    "TYRE_PRESSURE_FRONT_RIGHT": "219.9",
    "TYRE_PRESSURE_REAR_LEFT": "224.8",
    "TYRE_PRESSURE_REAR_RIGHT": "unknown",
    "VEHICLE_STATE_TYPE": "IGNITION_OFF",
    "LATITUDE": 40.0,
    "LONGITUDE": -100.0,
}


EXPECTED_STATE_EV_UNAVAILABLE = {
    "AVG_FUEL_CONSUMPTION": "unavailable",
    "DISTANCE_TO_EMPTY_FUEL": "unavailable",
    "EV_CHARGER_STATE_TYPE": "unavailable",
    "EV_CHARGE_SETTING_AMPERE_TYPE": "unavailable",
    "EV_CHARGE_VOLT_TYPE": "unavailable",
    "EV_DISTANCE_TO_EMPTY": "unavailable",
    "EV_IS_PLUGGED_IN": "unavailable",
    "EV_STATE_OF_CHARGE_MODE": "unavailable",
    "EV_STATE_OF_CHARGE_PERCENT": "unavailable",
    "EV_TIME_TO_FULLY_CHARGED_UTC": "unavailable",
    "ODOMETER": "unavailable",
    "TIMESTAMP": "unavailable",
    "TRANSMISSION_MODE": "unavailable",
    "TYRE_PRESSURE_FRONT_LEFT": "unavailable",
    "TYRE_PRESSURE_FRONT_RIGHT": "unavailable",
    "TYRE_PRESSURE_REAR_LEFT": "unavailable",
    "TYRE_PRESSURE_REAR_RIGHT": "unavailable",
    "VEHICLE_STATE_TYPE": "unavailable",
    "LATITUDE": "unavailable",
    "LONGITUDE": "unavailable",
}
