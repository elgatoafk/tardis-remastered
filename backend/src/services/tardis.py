from datetime import timedelta, datetime
from backend.src.logger import logger
from dateutil import parser, tz

from backend.src.config import settings


class TardisService:
    """Class for storing all time-related logic"""
    INPUT_FORMAT = "%H:%M:%S %d %B %Y (%A)"
    RESULT_FORMAT_PAST = settings.DATETIME_FORMAT_RESULT_PAST
    RESULT_FORMAT_FUTURE = settings.DATETIME_FORMAT_RESULT_FUTURE

    @staticmethod
    def convert_to_datetime(time_input: str, zone: str) -> datetime or None:
        """
        Converts a string containing date and time to a timezone-aware datetime object.

        Args:
            time_input (str): The input date and time as a string.
            zone (str): The timezone to convert to.

        Returns:
            datetime: A timezone-aware datetime object.
                      Returns None if the conversion fails.
        """
        try:

            time_input = parser.parse(time_input)

            target_timezone = tz.gettz(zone)

            if target_timezone is None:
                logger.error(f"Unable to find timezone for {time_input}")
                raise ValueError(f"Invalid timezone: {zone}")

            return time_input.astimezone(target_timezone)

        except (ValueError, TypeError, OverflowError) as e:

            logger.error(f"Error converting time '{time_input}' with timezone '{zone}': {e}")
            return None

    @staticmethod
    def calculate_difference(current_time: datetime, user_time: datetime) -> timedelta or None:
        """
        Calculates the difference between the current time in London timezone
        and the provided user time.

        Args:
            user_time (datetime): The user's provided datetime object.
            current_time (datetime): The current datetime object.

        Returns:
            timedelta: The difference between the current time and user_time.
                       If the input is invalid, returns None.
        """
        if isinstance(user_time, datetime) and user_time.tzinfo is not None:
            try:

                diff = current_time - user_time
                return diff
            except Exception as e:
                logger.error(f"Error calculating difference for {user_time}: {e}")
                return None
        else:
            logger.error(f"Invalid time input: {user_time}")
            return None

    @staticmethod
    def format_input_to_string(time_input: datetime) -> str or None:
        """
        Formats the provided datetime object into a specific string format.

        Args:
            time_input (datetime): The datetime object to format.

        Returns:
            str: The formatted datetime string.
                 Returns None if the input is invalid.
        """
        if isinstance(time_input, datetime):
            try:
                return time_input.strftime(TardisService.INPUT_FORMAT)
            except Exception as e:
                logger.error(f"Error formatting input for {time_input}: {e}")
                return None
        else:
            logger.error(f"Invalid time input: {time_input}")
            return None

    @staticmethod
    def format_results(delta: timedelta, pattern: str = RESULT_FORMAT_PAST) -> str or None:
        """
        Formats a timedelta object into a specified string pattern.

        Args:
            delta (timedelta): The time difference to be formatted.
            pattern (str): The string pattern to format the timedelta.
                           Supported placeholders are:
                           - {d}: days
                           - {h}: hours
                           - {m}: minutes
                           - {s}: seconds
            Defaults to RESULT_FORMAT_PAST.
        Returns:
            str: The formatted string according to the pattern.
                 Returns None if the input is invalid.
        """
        if not isinstance(delta, timedelta):
            logger.error(f"Invalid time input: {delta}")
            return None

        if not isinstance(pattern, str):
            logger.error(f"Invalid pattern input: {pattern}")
            return None

        try:

            d = {'d': delta.days}
            d['h'], rem = divmod(delta.seconds, 3600)
            d['m'], d['s'] = divmod(rem, 60)

            return pattern.format(**d)

        except KeyError as e:
            logger.error(f"Invalid pattern input: {pattern}")
            return None

        except Exception as e:
            logger.error(f"Error formatting input for {pattern}: {e}")
            return None

    @staticmethod
    def add_timedelta(dt: datetime, delta: timedelta) -> datetime or None:
        """
        Adds a timedelta to a datetime object.

        Args:
            dt (datetime): The datetime object to which the timedelta will be added.
            delta (timedelta): The timedelta object representing the time difference to add.

        Returns:
            datetime: The resulting datetime after adding the timedelta.
                      Returns None if the input is invalid.
        """
        if not isinstance(dt, datetime):
            logger.error(f"Invalid time input: {dt}")
            return None

        if not isinstance(delta, timedelta):
            logger.error(f"Invalid time input: {delta}")
            return None

        try:
            result = dt + delta
            return result

        except Exception as e:
            logger.error(f"Error formatting input for {dt}: {e}")
            return None
