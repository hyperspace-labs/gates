library ieee;
use ieee.std_logic_1164.all;

entity nand_gate is
  port(
    a, b : in std_logic;
    x : out std_logic
  );
end entity;

architecture rtl of nand_gate is
begin
  
  x <= a nand b;

end architecture;