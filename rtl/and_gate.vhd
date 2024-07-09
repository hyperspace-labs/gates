library ieee;
use ieee.std_logic_1164.all;

entity and_gate is
  port(
    a, b : in std_logic;
    y : out std_logic
  );
end entity;

architecture rtl of and_gate is
  
    component nand_gate
      port(
        a : in std_logic;
        b : in std_logic;
        x : out std_logic
      );
      end component;
    
    signal x : std_logic;

begin
    u1 : nand_gate
      port map(
        a => a,
        b => b,
        x => x
      );

    u2 : nand_gate
      port map(
        a => x,
        b => x,
        x => y
      );

end architecture;