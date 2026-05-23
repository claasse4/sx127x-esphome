#pragma once

#include "esphome/core/component.h"
#include "esphome/components/spi/spi.h"

namespace esphome {
namespace sx127x {

class SX127xComponent : public Component, public spi::SPIDevice {
 public:
  void setup() override;
  void loop() override;

  void set_cs_pin(GPIOPin *pin) { cs_pin_ = pin; }
  void set_rst_pin(GPIOPin *pin) { rst_pin_ = pin; }
  void set_dio0_pin(GPIOPin *pin) { dio0_pin_ = pin; }

  void set_frequency(uint32_t f) { frequency_ = f; }
  void set_modulation(const std::string &m) { modulation_ = m; }
  void set_bitsync(bool b) { bitsync_ = b; }
  void set_packet_mode(bool p) { packet_mode_ = p; }
  void set_rx_start(bool r) { rx_start_ = r; }
  void set_rx_floor(int f) { rx_floor_ = f; }
  void set_bandwidth(const std::string &bw) { bandwidth_ = bw; }
  void set_pa_pin(const std::string &p) { pa_pin_ = p; }
  void set_pa_power(int p) { pa_power_ = p; }

  void set_mode_tx();
  void set_mode_rx();
  void set_mode_sleep();
  void set_mode_standby();

 protected:
  GPIOPin *cs_pin_;
  GPIOPin *rst_pin_;
  GPIOPin *dio0_pin_;

  uint32_t frequency_;
  std::string modulation_;
  bool bitsync_;
  bool packet_mode_;
  bool rx_start_;
  int rx_floor_;
  std::string bandwidth_;
  std::string pa_pin_;
  int pa_power_;
};

}  // namespace sx127x
}  // namespace esphome
