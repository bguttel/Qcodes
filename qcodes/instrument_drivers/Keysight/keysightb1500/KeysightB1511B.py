from typing import TYPE_CHECKING, Any, Optional

from .constants import IMeasRange, IOutputRange
from .KeysightB1517A import KeysightB1517A

if TYPE_CHECKING:
    import qcodes.instrument_drivers.Keysight.keysightb1500


class KeysightB1511B(KeysightB1517A):
    """
    Driver for Keysight B1511B Source/Monitor Unit module for B1500
    Semiconductor Parameter Analyzer.

    Args:
        parent: mainframe B1500 instance that this module belongs to
        name: Name of the instrument instance to create. If `None`
            (Default), then the name is autogenerated from the instrument
            class.
        slot_nr: Slot number of this module (not channel number)
        asu_present: Flag to acknowledge ASU presence
    """

    def __init__(
        self,
        parent: "qcodes.instrument_drivers.Keysight.keysightb1500.KeysightB1500",
        name: Optional[str],
        slot_nr: int,
        **kwargs: Any
    ):
        super().__init__(parent, name, slot_nr, **kwargs)
        self._valid_i_measure_ranges: list[IMeasRange] = [
            IMeasRange.AUTO,
            IMeasRange.MIN_1nA,
            IMeasRange.MIN_10nA,
            IMeasRange.MIN_100nA,
            IMeasRange.MIN_1uA,
            IMeasRange.MIN_10uA,
            IMeasRange.MIN_100uA,
            IMeasRange.MIN_1mA,
            IMeasRange.MIN_10mA,
            IMeasRange.MIN_100mA,
            IMeasRange.FIX_1nA,
            IMeasRange.FIX_10nA,
            IMeasRange.FIX_100nA,
            IMeasRange.FIX_1uA,
            IMeasRange.FIX_10uA,
            IMeasRange.FIX_100uA,
            IMeasRange.FIX_1mA,
            IMeasRange.FIX_10mA,
            IMeasRange.FIX_100mA,
        ]
        self._asu_valid_i_measure_ranges: list[IMeasRange] = [
            IMeasRange.MIN_1pA, IMeasRange.MIN_10pA, IMeasRange.MIN_100pA,
            IMeasRange.FIX_1pA, IMeasRange.FIX_10pA, IMeasRange.FIX_100pA]
        self._valid_i_output_ranges: list[IOutputRange] = [
            IOutputRange.AUTO, IOutputRange.MIN_1nA, IOutputRange.MIN_10nA,
            IOutputRange.MIN_100nA, IOutputRange.MIN_1uA,
            IOutputRange.MIN_10uA, IOutputRange.MIN_100uA,
            IOutputRange.MIN_1mA, IOutputRange.MIN_10mA, IOutputRange.MIN_100mA]
        self._asu_valid_i_output_ranges: list[IOutputRange] = [
            IOutputRange.MIN_1pA, IOutputRange.MIN_10pA, IOutputRange.MIN_100pA]

        self.asu_present = False

    @property
    def asu_present(self) -> bool:
        return self._asu_present

    @asu_present.setter
    def asu_present(self, val: bool) -> None:
        if not isinstance(val, bool):
            raise TypeError("Expected: True or False")

        self._asu_present = val

        if self.asu_present:
            self._valid_i_measure_ranges = self._valid_i_measure_ranges + \
                                           self._asu_valid_i_measure_ranges
            self._valid_i_output_ranges = self._valid_i_output_ranges + \
                                          self._asu_valid_i_output_ranges
        else:
            self._valid_i_measure_ranges = list(
                set(self._valid_i_measure_ranges) -
                set(self._asu_valid_i_measure_ranges)
            )
            self._valid_i_output_ranges = list(
                set(self._valid_i_output_ranges) -
                set(self._asu_valid_i_output_ranges)
            )


B1511B = KeysightB1511B
"""
Alias for backwards compatibility
"""
