module snoopy_cache(rst,clk,cpu_bus_in,bus_rw_miss_wb_out);

input rst,clk;
//input bus_read_miss_in,bus_write_miss_in,cpu_read_hm,cpu_write_hm,cpu_read,cpu_write
input [5:0]cpu_bus_in;
output reg [2:0]bus_rw_miss_wb_out;
//2nd Bit - Read miss output
//1st Bit - Write miss output
//0th Bit - Write back


reg [2:0]present_state,next_state;

parameter invalid = 3'b001;
parameter shared = 3'b010;
parameter exclusive = 3'b100;

always@(posedge clk or negedge rst)
begin
	if(rst==1'b0)
	begin
		next_state <= invalid;
		bus_rw_miss_wb_out<=3'b000;
	end
	else
	case(present_state) 
		invalid: begin
						case(cpu_bus_in)
						6'b100000:begin next_state<=shared;
											 bus_rw_miss_wb_out<=3'b100;
						end
						6'b010000:begin next_state<= exclusive;
											 bus_rw_miss_wb_out<=3'b010;
						end
						default:begin next_state<= invalid;
											 bus_rw_miss_wb_out<=3'b010;
						end
						endcase
					end
		shared:  begin
//inp = {cpu_read,cpu_write,cpu_read_hm,cpu_write_hm,bus_read_miss_in,bus_write_miss_in}
						case(cpu_bus_in)
						6'b101000:begin next_state<= shared;
											 bus_rw_miss_wb_out<=3'b000;
						end
						6'b100000:begin next_state<= shared;
											 bus_rw_miss_wb_out<=3'b100;
						end
						6'b010100:begin next_state<= exclusive;
											 bus_rw_miss_wb_out<=3'b010;
						end
						6'b010000:begin next_state<= exclusive;
											 bus_rw_miss_wb_out<=3'b010;
						end
						6'b000010:begin next_state<= shared;
											 bus_rw_miss_wb_out<=3'b000;
						end
						6'b000001:begin next_state<= invalid;
											 bus_rw_miss_wb_out<=3'b000;
						end						
						default:begin next_state<= invalid;
											 bus_rw_miss_wb_out<=3'b000;
						end
						endcase
					end
		exclusive:begin
						case(cpu_bus_in)
						6'b101000:begin next_state<= exclusive;
											 bus_rw_miss_wb_out<=3'b000;
						end
						6'b100000:begin next_state<= shared;
											 bus_rw_miss_wb_out<=3'b101;
						end
						6'b010100:begin next_state<= exclusive;
											 bus_rw_miss_wb_out<=3'b000;
						end						
						6'b010000:begin next_state<= exclusive;
											 bus_rw_miss_wb_out<=3'b011;
						end
						6'b000010:begin next_state<= shared;
											 bus_rw_miss_wb_out<=3'b001;
						end						
						6'b000001:begin next_state<= invalid;
											 bus_rw_miss_wb_out<=3'b001;
						end	
						default:begin next_state<= invalid;
											 bus_rw_miss_wb_out<=3'b001;
						end
						endcase
					end
		default:begin
					next_state <= invalid;
					bus_rw_miss_wb_out <= 3'b000;
					end
					
	endcase	
present_state <= next_state;
end
endmodule