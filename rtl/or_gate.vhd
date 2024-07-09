library ieee;
use ieee.std_logic_1164.all;

library work;

entity or_gate is
  port(
    a, b : in std_logic;
    y : out std_logic
  );
end entity;

architecture rtl of or_gate is

  signal x1, x2 : std_logic;

begin
  -- 1st layer: This gate negates the first input 'a'.
  u1 : entity work.nand_gate
    port map(
      a => a,
      b => a,
      x => x1
    );

  -- 1st layer: This gate negates the second input 'b'.
  u2 : entity work.nand_gate
    port map(
      a => b,
      b => b,
      x => x2
    );
    
  -- 2nd layer: This gate produces the final output ('a' OR 'b').
  u3 : entity work.nand_gate
    port map(
      a => x1,
      b => x2,
      x => y
    );

end architecture;