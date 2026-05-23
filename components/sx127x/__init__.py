import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import spi
from esphome.const import *

CODEOWNERS = ["@coen"]

sx127x_ns = cg.esphome_ns.namespace("sx127x")
SX127xComponent = sx127x_ns.class_("SX127xComponent", cg.Component, spi.SPIDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SX127xComponent),
    cv.Required("cs_pin"): cv.pin,
    cv.Required("rst_pin"): cv.pin,
    cv.Required("dio0_pin"): cv.pin,
    cv.Required("frequency"): cv.int_range(min=100000000, max=1000000000),
    cv.Required("modulation"): cv.one_of("OOK", "FSK"),
    cv.Required("bitsync"): cv.boolean,
    cv.Optional("packet_mode", default=True): cv.boolean,
    cv.Optional("rx_start", default=False): cv.boolean,
    cv.Optional("rx_floor", default=-90): cv.int_,
    cv.Optional("bandwidth", default="50_0kHz"): cv.string,
    cv.Optional("pa_pin", default="BOOST"): cv.string,
    cv.Optional("pa_power", default=17): cv.int_range(min=2, max=20),
}).extend(spi.spi_device_schema())

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)

    cg.add(var.set_cs_pin(config["cs_pin"]))
    cg.add(var.set_rst_pin(config["rst_pin"]))
    cg.add(var.set_dio0_pin(config["dio0_pin"]))
    cg.add(var.set_frequency(config["frequency"]))
    cg.add(var.set_modulation(config["modulation"]))
    cg.add(var.set_bitsync(config["bitsync"]))
    cg.add(var.set_packet_mode(config["packet_mode"]))
    cg.add(var.set_rx_start(config["rx_start"]))
    cg.add(var.set_rx_floor(config["rx_floor"]))
    cg.add(var.set_bandwidth(config["bandwidth"]))
    cg.add(var.set_pa_pin(config["pa_pin"]))
    cg.add(var.set_pa_power(config["pa_power"]))
